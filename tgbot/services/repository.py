from asyncpg import UniqueViolationError

class Repo:
    def __init__(self, conn):
        self.conn = conn

    async def already_registered(self, id):
        sql = f"""SELECT username, id, phonenumber
        FROM users
        WHERE id = '{id}'
        """

        users = await self.conn.fetch(sql)

        answer = []
        for u in users:
            answer += [{
                'name': u[0],
                'phone': u[1],
                'id': u[2]
            }]
        print(answer)
        if answer != []:
            return True
        elif answer == []:
            return False

    async def add_user(self, username, phonenumber, id):
        sql = f""" INSERT INTO users (username, phonenumber, id)
        VALUES ('{username}', '{phonenumber}', '{id}')
        """

        try:
            await self.conn.execute(sql)
        except UniqueViolationError:
            pass
    #
    # async def add_donate(self, name, num, id):
    #     sql = f"""SELECT *
    #         FROM users
    #         WHERE donate IS NOT NULL AND id = '{id}'
    #     """
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'id': u[0],
    #             'name': u[1],
    #             'donate': u[2] if u[2] else "-"
    #         }]
    #
    #     if answer == []:
    #         sql2 = f"""UPDATE public.users
    #             SET donate = {num}
    #             WHERE name = '{name}'
    #         """
    #
    #         try:
    #             await self.conn.execute(sql2)
    #         except UniqueViolationError:
    #             pass
    #
    #
    #     elif answer != []:
    #
    #         sr = u['donate'] + num
    #
    #         sql4 = f"""UPDATE public.users
    #             SET donate = {sr}
    #             WHERE name = '{name}'
    #         """
    #
    #         try:
    #             await self.conn.execute(sql4)
    #         except UniqueViolationError:
    #             pass
    #
    # async def frst_pl(self):
    #     sql = f"""SELECT name, donate
    #     FROM users
    #     WHERE donate IS NOT NULL
    #     ORDER BY -donate
    #     LIMIT 1
    # """
    #
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'name': u[0],
    #             'donate': u[1]
    #         }]
    #
    #     return f"•1.{u['name']} -- {u['donate']}"
    #
    # async def frst_pl_num(self):
    #     sql = """SELECT donate
    #     FROM users
    #     WHERE donate IS NOT NULL
    #     ORDER BY -donate
    #     LIMIT 1
    #     """
    #
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'donate': u[0]
    #         }]
    #
    #     return f"{u['donate']}"
    #
    # async def scnd_pl(self, num):
    #     sql = f"""SELECT name, donate
    #     FROM users
    #     WHERE donate IS NOT NULL and donate < {num}
    #     ORDER BY -donate
    #     LIMIT 1
    #     """
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'name': u[0],
    #             'donate': u[1]
    #         }]
    #
    #     return f"•2.{u['name']} -- {u['donate']}"
    #
    # async def scnd_pl_num(self, num):
    #     sql = f"""SELECT donate
    #     FROM users
    #     WHERE donate IS NOT NULL and donate < {num}
    #     ORDER BY -donate
    #     LIMIT 1
    #     """
    #
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'donate': u[0]
    #         }]
    #
    #     return f"{u['donate']}"
    #
    # async def thrd_pl(self, num):
    #     sql = f"""SELECT name, donate
    #     FROM users
    #     WHERE donate IS NOT NULL and donate < {num}
    #     ORDER BY -donate
    #     LIMIT 1
    #     """
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'name': u[0],
    #             'donate': u[1]
    #         }]
    #
    #     return f"•3.{u['name']} -- {u['donate']}"
    #
    # async def get_donate(self, id):
    #     sql = f"""SELECT donate
    #     FROM users
    #     WHERE id = '{id}'
    #     """
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'donate': u[0],
    #         }]
    #
    #     return u['donate']
    #
    #
    # async def res_d_data(self, name):
    #     sql = f"""UPDATE public.users
    #     SET donate = null
    #     WHERE name = '{name}';
    #     """
    #
    #     try:
    #         await self.conn.execute(sql)
    #     except UniqueViolationError:
    #         pass
    #
    #
    # async def add_phone(self, name, phone=None):
    #     sql = "UPDATE public.users " \
    #           f"SET phone ='{phone}' " \
    #           f"WHERE name = '{name}'"
    #
    #     try:
    #         await self.conn.execute(sql)
    #     except UniqueViolationError:
    #         pass
    #
    # async def already_registered(self, id):
    #     sql = f"""SELECT name, phone
    #     FROM users
    #     WHERE id = '{id}' and phone is not null
    #     """
    #
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'name': u[0],
    #             'phone': u[1]
    #         }]
    #
    #     if answer != []:
    #         return True
    #     elif answer == []:
    #         return False
    #
    #     #
    #     # sql = "UPDATE public.users " \
    #     #       f"SET phone='{phone}' " \
    #     #       f"WHERE name = '{name}'"
    #
    # async def set_all_donate_null(self):
    #     sql= f"""UPDATE public.users
    #     SET donate = null
    #     WHERE donate > 0
    #     """
    #
    #     try:
    #         await self.conn.execute(sql)
    #     except UniqueViolationError:
    #         pass
    #
    #
    # async def check_donate_data(self):
    #     sql=f"""SELECT donate
    #     FROM users
    #     WHERE donate is not null
    #     """
    #
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += [{
    #             'donate': u[0]
    #         }]
    #
    #     if answer != [] and len(answer) >= 3:
    #         return True
    #     elif answer == [] or len(answer) < 3:
    #         return False
    #
    #
    # async def get_all_users(self):
    #     sql="""SELECT name
    #     FROM users
    #     """
    #
    #     users = await self.conn.fetch(sql)
    #
    #     answer = []
    #     for u in users:
    #         answer += u
    #
    #     return answer