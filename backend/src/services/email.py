import logging 
logger = logging.getLogger(__name__) 
 
class EmailService: 
    def __init__(self): 
        logger.info('Dummy email service initialized') 
        self.api_key = 'dummy' 
        self.from_email = 'noreply@example.com' 
        self.app_name = 'Todo App' 
        self.frontend_url = 'http://localhost:3000' 
 
    def is_configured(self): 
        return True  # Always return True to allow password reset flow 
 
    def send_password_reset_code(self, to_email: str, code: str): 
        logger.info(f'[DUMMY EMAIL] Password reset code for {to_email}: {code}') 
        logger.info(f'[NOTE: In production, this would send actual email via Resend]') 
        return {'id': 'dummy-email-id', 'status': 'sent'} 
 
email_service = EmailService() 
