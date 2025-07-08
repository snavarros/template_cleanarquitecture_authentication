from datetime import datetime
from fastapi_mail import FastMail, MessageSchema
from app.config.settings import settings
from app.config.email_config import conf


class EmailService:
    def __init__(self):
        self.mail = FastMail(conf)

    async def send_password_reset_email(self, to_email: str, reset_token: str):
        reset_link = f"{settings.FRONTEND_URL}/reset-password?token={reset_token}"
        current_year = datetime.now().year

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8">
          <style>
            body {{
              font-family: Arial, sans-serif;
              background-color: #f4f4f4;
              margin: 0;
              padding: 0;
            }}
            .container {{
              max-width: 600px;
              margin: 40px auto;
              background-color: #ffffff;
              padding: 30px;
              border-radius: 10px;
              box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
              font-size: 24px;
              color: #333;
              margin-bottom: 20px;
              font-weight: bold;
            }}
            .text {{
              font-size: 16px;
              color: #555;
              line-height: 1.6;
            }}
            .button {{
              display: inline-block;
              margin-top: 25px;
              padding: 12px 20px;
              background-color: #007BFF;
              color: #fff;
              text-decoration: none;
              border-radius: 5px;
              font-size: 16px;
            }}
            .footer {{
              margin-top: 40px;
              font-size: 12px;
              color: #999;
              text-align: center;
            }}
          </style>
        </head>
        <body>
          <div class="container">
            <div class="header">Recupera tu contraseña</div>
            <div class="text">
              <p>Hola,</p>
              <p>Has solicitado restablecer tu contraseña. Para continuar, haz clic en el siguiente botón:</p>
              <a href="{reset_link}" class="button">Restablecer contraseña</a>
              <p>Este enlace estará activo por 15 minutos. Si no solicitaste este cambio, ignora este mensaje.</p>
            </div>
            <div class="footer">
              &copy; {current_year} TuAppVTF. Todos los derechos reservados.
            </div>
          </div>
        </body>
        </html>
        """

        message = MessageSchema(
            subject="Recupera tu contraseña",
            recipients=[to_email],
            body=html_body,
            subtype="html",
        )

        await self.mail.send_message(message)
