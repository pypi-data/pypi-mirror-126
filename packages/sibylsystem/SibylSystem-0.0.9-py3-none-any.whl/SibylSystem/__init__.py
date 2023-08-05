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

from .types import TokenValidation, Ban, BanResult, Token, PermissionResponse
from .exceptions import GeneralException, InvalidTokenException, InvalidPermissionRangeException
__version__ = '0.0.9'

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
        r = self.client.get(f"{self.host}createToken?token={self.token}&user-id={user_id}&permission={permission}")
        if r.status_code != 200:
            raise GeneralException(r.json()["error"]["message"])
        return Token(**r.json()["result"])

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
        r = self.client.get(f"{self.host}changePerm?token={self.token}&user-id={user_id}&permission={permission}")
        if r.status_code != 200:
            raise GeneralException(r.json()["error"]["message"])
        return PermissionResponse(**r.json())
    
    def get_token(self, user_id: int):
        return self._token_method(
            'getToken?token=', user_id, "Failed to get token"
        )

    def _token_method(self, arg0, user_id, arg2):
        r = self.client.get(f'{self.host}{arg0}{self.token}&user-id={user_id}')
        if r.status_code != 200:
            raise GeneralException(arg2)
        return Token(**r.json()['result'])
        
    def add_ban(self, user_id: int, reason: str, message: str=None, source: str=None) -> BanResult:
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
        r = self.client.get(f"{self.host}addBan?token={self.token}&user-id={user_id}&reason={reason}&message={message}&source={source}")
        if r.status_code != 200:
            raise GeneralException(r.json()["error"]["message"])
        return BanResult(**r.json()["result"])
    
    def delete_ban(self, user_id: int) -> bool:
        """Unban a user

        Args:
            user_id (:obj:`int`): User ID of the user to be unbanned

        Raises:
            GeneralException

        Returns:
            bool
        """
        r = self.client.get(f"{self.host}removeBan?token={self.token}&user-id={user_id}")
        if r.status_code != 200:
            raise GeneralException(r.json()["error"]["message"])
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
        r = self.client.get(f"{self.host}getInfo?token={self.token}&user-id={user_id}")
        if r.status_code != 200:
            raise GeneralException(r.json()["error"]["message"])
        return Ban(**r.json()["result"])

    def report_user(self, user_id: int, reason: str, message: str=None) -> bool:
        """Report a user, on the API, to be worked upon by the inspectors

        Args:
            user_id (:obj:`int`): User Id of the user to be report
            reason (:obj:`str`): reason of the ban
            message (:obj:`str`, optional): [Ban message, basically the message the given user to be banned upon.]. Defaults to None.

        Raises:
            GeneralException

        Returns:
            bool
        """
        r = self.client.get(f"{self.host}reportUser?token={self.token}&user-id={user_id}&reason={reason}&message={message}")
        if r.status_code != 200:
            raise GeneralException(r.json()["error"]["message"])
        return True


    
