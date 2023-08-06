# SibylSystem-py

# Copyright (C) 2021 Sayan Biswas, AnonyIndian

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import httpx, typing

from .types import TokenValidation, Ban, BanResult, Token, PermissionResponse, StatsResult, BanRes, ReportResponse
from .exceptions import GeneralException, InvalidTokenException, InvalidPermissionRangeException
from urllib.parse import quote_plus
__version__ = '0.0.10'

class PsychoPass:
    """
    Class for the Sibyl API client
    
    Args:
        token (:obj:`str`): Sibyl API token
        host (:obj:`str`, optional): Sibyl API service URL.
        client (:obj:`httpx.Client`, optional): HTTPX client class.
        show_license (:obj:`bool`, optional): Defaults to true, set to false to hide copyright message
    """
    def __init__(self, token: str, host: typing.Optional[str] = "https://psychopass.animekaizoku.com/", client: typing.Optional[httpx.Client] = None, show_license: bool = True) -> None:
        if show_license:
            l = '''
    SibylSystem Copyright (C) 2021 Sayan Biswas, AnonyIndian
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.
            '''
            print(l)
        if not host.endswith("/"):
            host += "/"
        if not host.startswith("http"):
            host = "http://" + host
        self.host = host
        self.token = token
        self.client = client
        if not self.client:
            self.client = httpx.Client()
        if not self.check_token(self.token):
            raise InvalidTokenException()
    
    def check_token(self, token: str) -> bool:
        '''
        Check if Sibyl API token is valid
        
        Args:
            token (:obj:`str`): Sibyl API token

        Raises:
            InvalidTokenException

        Returns:
            bool: if the token is valid, it'll return True, else False
        '''
        r = self.client.get(f"{self.host}checkToken?token={token}")
        x = TokenValidation(**r.json())
        if not x.success:
            raise InvalidTokenException()
        return x.result

    def create_token(self, user_id: int, permission: int = 0) -> Token:
        """
        Create new token, with a user id and permission number
        
            0 = User,
            1 = Enforcer,
            2 = Inspector
        
        Args:
            user_id (:obj:`int`): User Id of the user for the token to be assigned to.
            permission (:obj:`int`, optional): [Permission of user]. Defaults to 0.

        Raises:
            InvalidPermissionRangeException
            GeneralException

        Returns:
            Token
        """
        if permission > 2:
            raise InvalidPermissionRangeException("Permission can be 0, 1, 2, not {}".format(permission))
        d = self._prepare_url(
            'createToken?token=', user_id, permission
        )

        return Token(**d["result"])

    def revoke_token(self, user_id: int):
        return self._token_method(
            'revokeToken?token=', user_id, "Failed to revoke token"
        )

    def change_permission(self, user_id: int, permission: int) -> PermissionResponse:
        """Change permission of given user
            
            0 = User,
            1 = Enforcer,
            2 = Inspector
            
        Args:
            user_id (:obj:`int`): User Id of the user to be promoted/demoted
            permission (:obj:`int`): new permission of user, can be 0, 1, 2

        Raises:
            GeneralException

        Returns:
            PermissionResponse
        """
        d = self._prepare_url(
            'changePerm?token=', user_id, permission
        )

        return PermissionResponse(**d)

    def _prepare_url(self, method, user_id, permission):
        r = self.client.get(
            f'{self.host}{method}{self.token}&user-id={user_id}&permission={permission}'
        )

        result = r.json()
        if result['success'] == False:
            raise GeneralException(result['error']['message'])
        return result
    
    def get_token(self, user_id: int):
        return self._token_method('getToken?token=', user_id)

    def _token_method(self, method, user_id):
        r = self.client.get(f'{self.host}{method}{self.token}&user-id={user_id}')
        d = r.json()
        if d["success"] == False:
            raise GeneralException(d['error']["message"])
        return Token(**d['result'])
        
    def add_ban(self, user_id: int, reason: str, message: str=None, source: str=None) -> BanRes:
        """Add a new ban to database

        Args:
            user_id (:obj:`int`): User Id of the user to be banned
            reason (:obj:`str`): reason of the ban
            message (:obj:`str`, optional): [Ban message, basically the message the given user was banned upon.]. Defaults to None.
            source (:obj:`str`, optional): [Ban source, the message link to the message the user was banned upon]. Defaults to None.

        Raises:
            GeneralException

        Returns:
            BanResult
        """
        r = self.client.get(f"{self.host}addBan?token={self.token}&user-id={user_id}&reason={quote_plus(reason)}&message={quote_plus(message) if message else None}&source={quote_plus(source) if source else None}")
        d = BanResult(**r.json())
        if not d.success:
            raise GeneralException(d.error["message"])
        return d.result
    
    def delete_ban(self, user_id: int) -> bool:
        """Unban a user

        Args:
            user_id (:obj:`int`): User ID of the user to be unbanned

        Raises:
            GeneralException

        Returns:
            bool
        """
        r = self._check_response('removeBan?token=', user_id)
        return True
    
    def get_info(self, user_id: int) -> Ban:
        """Get info about a user on the API

        Args:
            user_id (:obj:`int`): User ID of the user to be looked up

        Raises:
            GeneralException

        Returns:
            Ban
        """
        r = self._check_response('getInfo?token=', user_id)
        return Ban(**r.json()["result"])

    def _check_response(self, method, user_id):
        result = self.client.get(f'{self.host}{method}{self.token}&user-id={user_id}')
        d = result.json()
        if d['success'] == False:
            raise GeneralException(d['error']['message'])
        return result

    def report_user(self, user_id: int, reason: str, message: str, source_url: str = None, is_bot: typing.Optional[bool] = False) -> bool:
        """Report a user, on the API, to be worked upon by the inspectors

        Args:
            user_id (:obj:`int`): User Id of the user to be report
            reason (:obj:`str`): reason of the ban
            message (:obj:`str`): Ban message, basically the message the given user to be banned upon.
            source_url (:obj:`str`, optional): Ban source, the message link to the message the user was banned upon.
            is_bot (:obj:`bool`, optional): [Is the user a bot?]. Defaults to False.

        Raises:
            GeneralException

        Returns:
            bool
        """
        r = self.client.get(f"{self.host}reportUser?token={self.token}&user-id={user_id}&reason={quote_plus(reason)}&message={quote_plus(message)}&src={quote_plus(source_url) if source_url else None}&isBot={is_bot}")
        d = ReportResponse(**r.json())
        if d.success:
            return True
        raise GeneralException(d.error["message"])
    
    def get_stats(self) -> StatsResult:
        """Get stats from API

        Raises:
            GeneralException

        Returns:
            StatsResult
        """
        r = self.client.get(f"{self.host}stats?token={self.token}")
        d = StatsResult(**r.json())
        if d.success:
            return d
        raise GeneralException(d.error["message"])