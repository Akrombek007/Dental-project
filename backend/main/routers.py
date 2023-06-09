from .services import auth_service, authorized_admin_service, authorized_register_service, authorized_doctor_service
from registration_repository import AuthorizedRegisterServiceRouter
from doctor_repository.wrappers import AuthorizedDoktorServiceRouter
from admin_service import AuthorizedAdminServiceRouter
from auth_service import AuthServiceRouter
from fastapi import APIRouter

auth_service_router = AuthServiceRouter(auth_service=auth_service)
authorized_admin_service_router = AuthorizedAdminServiceRouter(authorized_admin_service=authorized_admin_service)
authorized_register_service_router = AuthorizedRegisterServiceRouter(authorized_register_service=authorized_register_service)
authorized_doctor_service_router = AuthorizedDoktorServiceRouter(authorized_doctor_service)
router = APIRouter()
router.include_router(auth_service_router)
router.include_router(authorized_admin_service_router)
router.include_router(authorized_register_service_router)
router.include_router(authorized_doctor_service_router)