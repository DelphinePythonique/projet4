from router import Router
import fixtures

if __name__ == "__main__":
    router = Router()
    context = {'route': 'homepage'}
    while 'route' in context:
        context = router.call_controller_method(context)

