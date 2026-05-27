import json
import urllib.parse
import boto3

# Inicializa o cliente do S3 usando a biblioteca boto3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Função executada automaticamente quando um novo objeto é criado no S3.
    """
    print("Evento recebido com sucesso!")
    
    try:
        # 1. Extrai o nome do bucket e o nome do arquivo (key) a partir do evento do S3
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        
        # O nome do arquivo pode vir com caracteres especiais codificados (ex: espaços como '+')
        file_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        
        print(f"Bucket detectado: {bucket_name}")
        print(f"Arquivo detectado: {file_key}")
        
        # 2. Busca os metadados do objeto diretamente no S3
        response = s3_client.head_object(Bucket=bucket_name, Key=file_key)
        file_type = response.get('ContentType', 'Desconhecido')
        file_size = response.get('ContentLength', 0)
        
        print(f"Tipo do arquivo: {file_type}")
        print(f"Tamanho do arquivo: {file_size} bytes")
        
        # Retorno de sucesso para a execução do Lambda
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Automação executada com sucesso!',
                'bucket': bucket_name,
                'file': file_key,
                'type': file_type
            })
        }

    except Exception as e:
        print(f"Erro ao processar o arquivo do S3: {str(e)}")
        raise e
