from sqlalchemy import create_engine, text

db_connetion_string = "mysql+pymysql://e6vd8bm43h3wxw4y9sg7:pscale_pw_IcKJrdGFSX115UH9bdFD8SXvI775onZtctnh0AJHn4y@aws.connect.psdb.cloud/febricareers?charset=utf8mb4"

engine = create_engine(
    db_connetion_string,
    connect_args = {
        'ssl': {
            'ca': '/etc/ssl/cert.pem'
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    
    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))

    print(result_dicts)