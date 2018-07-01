from django.db.models.signals import post_save, pre_save
from communication.models import UserQuestion, QuestionConfig, QuestionComment
from django.dispatch import receiver


@receiver(pre_save, sender=UserQuestion)
def comment_add(sender, instance, **kwargs):
    if instance.is_closed and not instance.end_message:
        content = QuestionConfig.get_solo().message
        message = QuestionComment.objects.filter(content=content).first()
        if not message:
            message = QuestionComment.objects.create(content=content, is_admin=True)
        instance.end_message = message
        instance.end_message.save()
    elif not instance.is_closed and instance.end_message:
        instance.end_message = None

    if instance.is_read == 'force read':
        instance.is_read = 'read'
    else:
        instance.is_read = '!read'

