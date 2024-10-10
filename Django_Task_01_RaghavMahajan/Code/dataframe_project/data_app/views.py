import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .models import DataFrameModel

def upload_dataframe(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read CSV into DataFrame
            df = pd.read_csv(request.FILES['file'])

            # Save each row in the DataFrame to the database
            for _, row in df.iterrows():
                DataFrameModel.objects.create(
                    column_1=row['column_1'],
                    column_2=row['column_2'],
                    column_3=row['column_3'],
                    column_4=row['column_4']
                )
            return render(request, 'data_app/success.html')
    else:
        form = UploadFileForm()
    return render(request, 'data_app/upload.html', {'form': form})

def show_data(request):
    data = DataFrameModel.objects.all()
    return render(request, 'data_app/show_data.html', {'data': data})
