import os
import datetime
import shutil

def main():
    try:

        today_date = datetime.date.today().strftime('%Y%m%d')
        incoming_files_path = f'../incoming_files/{today_date}'
        email_date = datetime.date.today().strftime('%Y-%m-%d')
        subject = f'Validation email for {email_date}'
        incoming_files = os.listdir(incoming_files_path)
        success_files_path = f'../success_files/{today_date}'
        rejected_files_path = f'../rejected_files/{today_date}'
        total_cnt = len(incoming_files)
 if total_cnt > 0:
            success_cnt = 0
            rejected_cnt = 0
            for file in incoming_files:

                flag = True
                header = False
                products = v.read_master_data()
                with open(f'{incoming_files_path}/{file}') as f:
                    orders = f.readlines()[1:]

                    if len(orders) > 0:
                        for order in orders:

                            rejected_reason = ''
                            pid_reject_reason = ''
                            empty_reject_reason = ''
                            date_reject_reason = ''
                            city_reject_reason = ''
                            sales_reject_reason = ''
                            order_dict = {}

                            data_row = order.split(',')
                            order_dict['order_id'] = data_row[0]
                            order_dict['order_date'] = data_row[1]
                            order_dict['product_id'] = data_row[2]
                            order_dict['quantity'] = data_row[3]
                            order_dict['sales'] = data_row[4]
                            order_dict['city'] = data_row[5].strip()

                            val_pid = v.validate_product_id(order_dict['product_id'], products)
                            val_od = v.validate_order_date(order_dict['order_date'])
                            val_city = v.validate_city(order_dict['city'])
                            val_empty = v.validate_emptiness(order_dict)
                            val_sales = v.validate_sales(order_dict)

                            if not val_pid:
                                pid_reject_reason = f"Invalid product id {order_dict['product_id']}"
                                rejected_reason = rejected_reason + pid_reject_reason + ';'
                            if len(val_empty) > 0:
                                for col in val_empty:
                                    empty_reject_reason = empty_reject_reason + col + ','
                                empty_reject_reason = 'Columns ' + empty_reject_reason.strip(',') + ' are empty.'
                                rejected_reason = rejected_reason + empty_reject_reason + ';'
                            if not val_od:
                                date_reject_reason = f"Date {order_dict['order_date']} is a future date."
                                rejected_reason = rejected_reason + date_reject_reason + ';'
                            if not val_city:
                                city_reject_reason = f"Invalid city {order_dict['city']}."
                                rejected_reason = rejected_reason + city_reject_reason + ';'
                            if not val_sales and val_pid:
                                sales_reject_reason = f'Invalid Sales calculation.'
                                rejected_reason = rejected_reason + sales_reject_reason

                            if val_pid and val_od and val_city and len(val_empty) == 0 and val_sales:
                                continue
