def get_object_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
    except model.MultipleObjectsReturned:
        return model.objects.filter(**kwargs).first()
    except Exception as e:
        return None
    return None