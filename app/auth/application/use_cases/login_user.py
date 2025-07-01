class LoginUser:
    def __init__(self, repo, auth_service):
        self.repo = repo
        self.auth = auth_service

    async def execute(self, dto):
        db_user = await self.repo.find_by_email(dto.email)
        if not db_user or not self.auth.verify_password(
            dto.password, db_user.hashed_password
        ):
            raise Exception("Invalid credentials")
        return self.auth.create_token(db_user.email)
