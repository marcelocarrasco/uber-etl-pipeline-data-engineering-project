from sqlalchemy import create_engine, event

def get_engine(params):
    
    DIALECT                 = 'oracle'
    SQL_DRIVER              = 'cx_oracle'
    USERNAME                = params.user
    PASSWORD                = params.password
    HOST                    = params.host
    PORT                    = params.port
    SERVICE                 = params.db
    ENGINE_PATH_WIN_AUTH    = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

    return create_engine(ENGINE_PATH_WIN_AUTH)
def get_engine():
    DIALECT                 = 'oracle'
    SQL_DRIVER              = 'cx_oracle'
    USERNAME                = 'mcarrasco'
    PASSWORD                = 'Pa$$4dba'
    HOST                    = '192.168.56.1'
    PORT                    = 1521
    SERVICE                 = 'dtc_pdb'
    ENGINE_PATH_WIN_AUTH    = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

    return create_engine(ENGINE_PATH_WIN_AUTH)
