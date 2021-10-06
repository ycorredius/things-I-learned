import csv
import os


def read_csv(file):
    print(file)
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if not row[9][0].isalpha():
                write_csv(row)


def create_dir(dir_name):
    parent_dir = "P:\\Vendors\\Edwards"
    new_dir_name = f'{dir_name}'
    path = os.path.join(parent_dir, new_dir_name)
    os.mkdir(path)
    print(f'{path}. Created')
    return


def write_csv(row):
    parent_directory = f'P:\\Vendors\\Edwards\\{row[4]}'
    if os.path.isdir(parent_directory):
        if os.path.isfile(f'{parent_directory}\\PD1-Product-skus.csv'):
            with open(f'{parent_directory}\\PD1-Product-skus.csv', mode='a') as file:
                header_names = ['ProductName', 'ProductDescription', 'Brand', 'Supplier', 'DNProductType',
                                'VendorProductCode', 'ColorName', 'SizeCode', 'SizeName', 'ColorPaletteName',
                                'LifeStyleImage', 'DecorationTemplate1', 'ViewSrc1', 'PiecePrice',
                                'Category', 'ShippingLength', 'ShippingWidth', 'ShippingHeight', 'ShippingWeight',
                                'GTIN']
                product_sku = row[1].replace(' ', '-')
                writer = csv.DictWriter(file, fieldnames=header_names)
                writer.writerow(dict(ProductName=row[18], ProductDescription=row[17], Brand=row[16], Supplier=row[16],
                                     DNProductType='Apparel', VendorProductCode=product_sku, ColorName=row[19],
                                     SizeCode=row[6], SizeName=row[6], ColorPaletteName='PD2-Color-Value-hex.csv',
                                     LifeStyleImage=f'{product_sku}.jpg', DecorationTemplate1=f'{product_sku}.jpg',
                                     ViewSrc1=f'{product_sku}.jpg', PiecePrice=f'{row[9]}',
                                     Category='Workwear | Shirt | Unisex', ShippingLength=f'{row[15]}',
                                     ShippingWidth=f'{row[34]}', ShippingHeight=f'{row[14]}',
                                     ShippingWeight=f'{row[13]}'))
        else:
            with open(f'{parent_directory}\\PD1-Product-skus.csv', mode='w') as file:
                header_names = ['ProductName', 'ProductDescription', 'Brand', 'Supplier', 'DNProductType',
                                'VendorProductCode', 'ColorName', 'SizeCode', 'SizeName', 'ColorPaletteName',
                                'LifeStyleImage', 'DecorationTemplate1', 'ViewSrc1', 'PiecePrice',
                                'Category', 'ShippingLength', 'ShippingWidth', 'ShippingHeight', 'ShippingWeight',
                                'GTIN']
                writer = csv.DictWriter(file, fieldnames=header_names)
                writer.writeheader()
                write_csv(row)
    else:
        print("Not a directory")
        create_dir(row[4])
        print('Back to else statement!')
        write_csv(row)


if __name__ == '__main__':
    csv_file = input("What file would you like to read?")
    read_csv(csv_file)
