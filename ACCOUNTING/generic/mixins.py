from django.views.generic.base import ContextMixin

class ContextPageMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(ContextPageMixin, self).get_context_data(**kwargs)
        context['pagename'] = self.pagename
        return context
