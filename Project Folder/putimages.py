import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Christiano Ronaldo'),
      ('image2.jpg','Christiano Ronaldo'),
      ('image3.jpg','Leonardo De Caprio'),
      ('image4.jpg','Leonardo De Caprio'),
      ('image5.jpg','Elon Musk'),
      ('image6.jpg','Elon Musk')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('influencerss-images','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})