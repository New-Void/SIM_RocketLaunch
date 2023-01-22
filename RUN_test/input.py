
exec(open("Modified_data/realtime.py").read())
exec(open("Modified_data/rocket.dr").read())

trick.trick_view_add_auto_load_file("TV_rocket.tv")
trick.stop(800)


varServerPort = trick.var_server_get_port()
RocketDisplay_path = os.environ['HOME'] + "/trick_sims/SIM_rocket_launch/models/rocket/graphics/Rocket/Build/Rocket.exe"
if (os.path.isfile(RocketDisplay_path)) :
    RocketDisplay_cmd = RocketDisplay_path + " " + str(varServerPort) + " &" 
    print(RocketDisplay_cmd)
    os.system( RocketDisplay_cmd)
else :
    print('Oops! Can\'t find ' + RocketDisplay_cmd )