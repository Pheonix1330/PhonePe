import os
import json
import mysql.connector

# MYSQL CONNECTION

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokesh9090@",
    database="phonepe"
)

cursor = conn.cursor()

base_path = "pulse-master/data"


# FUNCTION


def execute_query(query, values):
    try:
        cursor.execute(query, values)
    except:
        pass


# 1. AGGREGATED TRANSACTION


path = base_path + "/aggregated/transaction/country/india/state"

for state in os.listdir(path):

    state_path = path + "/" + state

    for year in os.listdir(state_path):

        year_path = state_path + "/" + year

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = int(file.strip(".json"))

                with open(year_path + "/" + file, "r") as f:

                    data = json.load(f)

                    try:
                        for item in data["data"]["transactionData"]:

                            query = """
                            INSERT INTO aggregated_transaction
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """

                            values = (
                                state,
                                year,
                                quarter,
                                item["name"],
                                item["paymentInstruments"][0]["count"],
                                item["paymentInstruments"][0]["amount"]
                            )

                            execute_query(query, values)

                    except:
                        pass


# 2. AGGREGATED USER


path = base_path + "/aggregated/user/country/india/state"

for state in os.listdir(path):

    state_path = path + "/" + state

    for year in os.listdir(state_path):

        year_path = state_path + "/" + year

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = int(file.strip(".json"))

                with open(year_path + "/" + file, "r") as f:

                    data = json.load(f)

                    try:
                        for item in data["data"]["usersByDevice"]:

                            query = """
                            INSERT INTO aggregated_user
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """

                            values = (
                                state,
                                year,
                                quarter,
                                item["brand"],
                                item["count"],
                                item["percentage"]
                            )

                            execute_query(query, values)

                    except:
                        pass


# 3. AGGREGATED INSURANCE


path = base_path + "/aggregated/insurance/country/india/state"

if os.path.exists(path):

    for state in os.listdir(path):

        state_path = path + "/" + state

        for year in os.listdir(state_path):

            year_path = state_path + "/" + year

            for file in os.listdir(year_path):

                if file.endswith(".json"):

                    quarter = int(file.strip(".json"))

                    with open(year_path + "/" + file, "r") as f:

                        data = json.load(f)

                        try:
                            for item in data["data"]["transactionData"]:

                                query = """
                                INSERT INTO aggregated_insurance
                                VALUES (%s,%s,%s,%s,%s,%s)
                                """

                                values = (
                                    state,
                                    year,
                                    quarter,
                                    item["name"],
                                    item["paymentInstruments"][0]["count"],
                                    item["paymentInstruments"][0]["amount"]
                                )

                                execute_query(query, values)

                        except:
                            pass


# 4. MAP USER


path = base_path + "/map/user/hover/country/india/state"

for state in os.listdir(path):

    state_path = path + "/" + state

    for year in os.listdir(state_path):

        year_path = state_path + "/" + year

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = int(file.strip(".json"))

                with open(year_path + "/" + file, "r") as f:

                    data = json.load(f)

                    try:
                        for district, values_data in data["data"]["hoverData"].items():

                            query = """
                            INSERT INTO map_user
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """

                            values = (
                                state,
                                year,
                                quarter,
                                district,
                                values_data["registeredUsers"],
                                values_data["appOpens"]
                            )

                            execute_query(query, values)

                    except:
                        pass


# 5. MAP TRANSACTION


path = base_path + "/map/transaction/hover/country/india/state"

for state in os.listdir(path):

    state_path = path + "/" + state

    for year in os.listdir(state_path):

        year_path = state_path + "/" + year

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = int(file.strip(".json"))

                with open(year_path + "/" + file, "r") as f:

                    data = json.load(f)

                    try:
                        for item in data["data"]["hoverDataList"]:

                            query = """
                            INSERT INTO map_transaction
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """

                            values = (
                                state,
                                year,
                                quarter,
                                item["name"],
                                item["metric"][0]["count"],
                                item["metric"][0]["amount"]
                            )

                            execute_query(query, values)

                    except:
                        pass


# 6. MAP INSURANCE


path = base_path + "/map/insurance/hover/country/india/state"

if os.path.exists(path):

    for state in os.listdir(path):

        state_path = path + "/" + state

        for year in os.listdir(state_path):

            year_path = state_path + "/" + year

            for file in os.listdir(year_path):

                if file.endswith(".json"):

                    quarter = int(file.strip(".json"))

                    with open(year_path + "/" + file, "r") as f:

                        data = json.load(f)

                        try:
                            for item in data["data"]["hoverDataList"]:

                                query = """
                                INSERT INTO map_insurance
                                VALUES (%s,%s,%s,%s,%s,%s)
                                """

                                values = (
                                    state,
                                    year,
                                    quarter,
                                    item["name"],
                                    item["metric"][0]["count"],
                                    item["metric"][0]["amount"]
                                )

                                execute_query(query, values)

                        except:
                            pass


# 7. TOP USER


path = base_path + "/top/user/country/india/state"

for state in os.listdir(path):

    state_path = path + "/" + state

    for year in os.listdir(state_path):

        year_path = state_path + "/" + year

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = int(file.strip(".json"))

                with open(year_path + "/" + file, "r") as f:

                    data = json.load(f)

                    try:
                        for item in data["data"]["pincodes"]:

                            query = """
                            INSERT INTO top_user
                            VALUES (%s,%s,%s,%s,%s)
                            """

                            values = (
                                state,
                                year,
                                quarter,
                                item["name"],
                                item["registeredUsers"]
                            )

                            execute_query(query, values)

                    except:
                        pass


# 8. TOP MAP


path = base_path + "/top/transaction/country/india/state"

for state in os.listdir(path):

    state_path = path + "/" + state

    for year in os.listdir(state_path):

        year_path = state_path + "/" + year

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = int(file.strip(".json"))

                with open(year_path + "/" + file, "r") as f:

                    data = json.load(f)

                    try:
                        for item in data["data"]["districts"]:

                            query = """
                            INSERT INTO top_map
                            VALUES (%s,%s,%s,%s,%s,%s)
                            """

                            values = (
                                state,
                                year,
                                quarter,
                                item["entityName"],
                                item["metric"]["count"],
                                item["metric"]["amount"]
                            )

                            execute_query(query, values)

                    except:
                        pass


# 9. TOP INSURANCE


path = base_path + "/top/insurance/country/india/state"

if os.path.exists(path):

    for state in os.listdir(path):

        state_path = path + "/" + state

        for year in os.listdir(state_path):

            year_path = state_path + "/" + year

            for file in os.listdir(year_path):

                if file.endswith(".json"):

                    quarter = int(file.strip(".json"))

                    with open(year_path + "/" + file, "r") as f:

                        data = json.load(f)

                        try:
                            for item in data["data"]["districts"]:

                                query = """
                                INSERT INTO top_insurance
                                VALUES (%s,%s,%s,%s,%s,%s)
                                """

                                values = (
                                    state,
                                    year,
                                    quarter,
                                    item["entityName"],
                                    item["metric"]["count"],
                                    item["metric"]["amount"]
                                )

                                execute_query(query, values)

                        except:
                            pass

conn.commit()

cursor.close()

conn.close()

print("ALL 9 TABLES DATA INSERTED SUCCESSFULLY")