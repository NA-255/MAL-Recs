import runpy
import traceback

print('Runner starting')
try:
    runpy.run_path('group_user_anime.py', run_name='__main__')
except Exception:
    traceback.print_exc()
print('Runner finished')
