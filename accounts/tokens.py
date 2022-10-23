import six  #pip install six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# 이메일 인증을 위한 token 발급
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
  def _make_hash_value(self, user, timestamp):
      return (
              six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
      )
      
account_activation_token = AccountActivationTokenGenerator()