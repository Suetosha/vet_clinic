from django.core.exceptions import PermissionDenied


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class GroupRequiredMixin(object):

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name=self.group_required).exists():
            return super().dispatch(request, *args, **kwargs)

        else:
            raise PermissionDenied()


