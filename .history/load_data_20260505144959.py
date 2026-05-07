import os
import json
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokesh9090@",
    database="phonepe"
)
cursor = conn.cursor()

# Path to your dataset
base_path = "D:/PhonePe/pulse-master/data/aggregated/transaction/country/india/state"

# Loop through states
for state in os.listdir(base_path):
    state_path = os.path.join(base_path, state)

    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)

        for file in os.listdir(year_path):
            if file.endswith(".json"):
                quarter = int(file.replace(".json", ""))
                file_path = os.path.join(year_path, file)

                with open(file_path, "r") as f:
                    data = json.load(f)

                    try:
                        for item in data["data"]["transactionData"]:
                            name = item["name"]
                            count = item["paymentInstruments"][0]["count"]
                            amount = item["paymentInstruments"][0]["amount"]

                            query = """
                            INSERT INTO aggregated_transaction
                            (state, year, quarter, transaction_type, transaction_count, transaction_amount)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """

                            values = (state, year, quarter, name, count, amount)
                            cursor.execute(query, values)

                    except:
                        continue

# Save data
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")