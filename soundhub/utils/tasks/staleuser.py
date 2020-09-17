from django.utils import timezone

from config import celery_app

__all__ = (
    'delete_staleuser',
)


@celery_app.task
def delete_staleuser():
    """
    A.K.I 가 생성된 유저를 조회하면서 stale user 를 삭제하는 메서드
    (stale user: 회원가입 후 이메일 인증을 하지 않은 채 오래 지난 유저)

    :return: None
    """
    # 이 함수가 users.models 에서 쓰이기 때문에, global 선언은 로드될 때 충돌을 야기한다.
    from users.models import ActivationKeyInfo

    for aki in ActivationKeyInfo.objects.all():
        if aki.user.is_active is False and aki.expires_at < timezone.now():
            aki.delete()

