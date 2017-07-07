class SavePathMiddleWare:
    def process_request(self,request):
        if request.path not in ['/user/login/',
                                '/user/register/',
                                '/user/logout/',
                                '/user/register_handle/',
                                '/user/login_handle/',
                                '/user/isvalid/',]:
            request.session['path']=request.get_full_path()
