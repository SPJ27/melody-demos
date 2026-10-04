from melody import Response, cookie

def index(request):
    return Response({'success': True}, status=201, headers={'test': 'xyz'}, cookies=[cookie('session_id', value='xyz', httponly=True)])

routes = {
    'GET /': index
}