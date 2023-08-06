import logging
from typing import TYPE_CHECKING, Dict, Optional

from . import project
from . import _auth
from .util import ExpirationTimer

if TYPE_CHECKING:
    from . import Project

logger = logging.getLogger(__name__)


class User:
    """
    ForecastFlow user class
    """

    def __init__(self, email: str, password: str) -> None:
        """
        Instantiate object with e-mail and password.

        Args:
            email:
                e-mail to sign in.

            password:
                password for sign in.
        """
        res = _auth.sign_in_with_password(email, password)
        self._id_token: str = res['idToken']
        self.user_id: str = res['localId']
        self._refresh_token: str = res['refreshToken']
        self._expiration_timer = ExpirationTimer(
            int(res['expiresIn']) - 10
        )  # refresh 10 seconds earlier
        self._projects: Dict[str, 'Project'] = {}

    def get_project(self, project_id: str, team_id: Optional[str] = None) -> 'Project':
        """
        Get project with given pid.

        Args:
            project_id:
                Project ID you want to open.

        Returns:
            ForecastFlow Project object with given pid.
        """
        if project_id not in self._projects:
            self._projects[project_id] = project.Project(self, project_id, team_id)
        return self._projects[project_id]

    @property
    def id_token(self) -> str:
        """
        This method refreshes a ID token if expired.
        """
        if self._expiration_timer.is_expired:
            logger.info('ID Token is expired. Refreshing.')
            res = _auth.refresh_id_token(self._refresh_token)
            id_token: str = res['id_token']
            self._id_token = id_token
            self._expiration_timer = ExpirationTimer(
                int(res['expires_in']) - 10  # refresh 10 seconds earlier
            )
        return self._id_token

    @property
    def uid(self) -> str:
        return self.user_id
