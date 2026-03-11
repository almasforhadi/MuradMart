from .models import Cart

""" def cart_items_count(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            return {'cart_items_count' : cart.get_total_items()}
        except Cart.DoesNotExist:
            # Fixed: Added missing return statement - was returning None before
            return {'cart_items_count' : 0}
    return {'cart_items_count' : 0} """

def cart_items_count(request):
    count = 0

    try:
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user).first()
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart = Cart.objects.filter(session_key=session_key).first()

        if cart:
            count = cart.items.count()
    except Exception:
        count = 0

    return {
        'cart_items_count': count
    }