# Importa Pandas para análise
import pandas as pd
# Lê os dados
data = pd.read_csv("pcap.csv")
# Verificando todas as colunas
data.columns
# Selecionando apenas os dados com benignos e de ataque DoS slowloris.
datafinal = data[data[' Label'].isin(['DoS slowloris', 'BENIGN'])]
# Indexando colunas para análise via group_by
index1 = [' Destination Port', ' Flow Duration', ' Total Fwd Packets',
' Total Backward Packets', 'Total Length of Fwd Packets',' Total Length of Bwd Packets', ' Fwd Packet Length Max',
' Fwd Packet Length Min', ' Fwd Packet Length Mean',
' Fwd Packet Length Std', 'Bwd Packet Length Max',
' Bwd Packet Length Min', ' Bwd Packet Length Mean',
' Bwd Packet Length Std', 'Flow Bytes/s', ' Flow Packets/s',
' Flow IAT Mean', ' Flow IAT Std']
index2 = [' Flow IAT Max', ' Flow IAT Min',
'Fwd IAT Total', ' Fwd IAT Mean', ' Fwd IAT Std', ' Fwd IAT Max',
' Fwd IAT Min', 'Bwd IAT Total', ' Bwd IAT Mean', ' Bwd IAT Std',
' Bwd IAT Max', ' Bwd IAT Min', 'Fwd PSH Flags', ' Bwd PSH Flags',' Fwd URG Flags', ' Bwd URG Flags', '
Fwd Header Length',
' Bwd Header Length', 'Fwd Packets/s', ' Bwd Packets/s',]
index3 = [ ' Min Packet Length', ' Max Packet Length', ' Packet Length Mean',
' Packet Length Std', ' Packet Length Variance', 'FIN Flag Count',
' SYN Flag Count', ' RST Flag Count', ' PSH Flag Count',
' ACK Flag Count', ' URG Flag Count', ' CWE Flag Count',
' ECE Flag Count', ' Down/Up Ratio', ' Average Packet Size',
' Avg Fwd Segment Size', ' Avg Bwd Segment Size',
' Fwd Header Length.1', 'Fwd Avg Bytes/Bulk', ' Fwd Avg Packets/Bulk']
index4 = [' Fwd Avg Bulk Rate', ' Bwd Avg Bytes/Bulk', ' Bwd Avg Packets/Bulk',
'Bwd Avg Bulk Rate', 'Subflow Fwd Packets', ' Subflow Fwd Bytes',
' Subflow Bwd Packets', ' Subflow Bwd Bytes', 'Init_Win_bytes_forward',
' Init_Win_bytes_backward', ' act_data_pkt_fwd',
' min_seg_size_forward', 'Active Mean', ' Active Std', ' Active Max',
' Active Min', 'Idle Mean', ' Idle Std', ' Idle Max', ' Idle Min']
datafinal.groupby([' Label'])[index1].max() #median e min também
datafinal.groupby([' Label'])[index2].max() #median e min também
datafinal.groupby([' Label'])[index3].max() #median e min também
datafinal.groupby([' Label'])[index4].max() #median e min também
# Gerando base com colunas escolhidas
base = datafinal[[' Destination Port', ' Flow Duration', 'Total Length of Fwd Packets', ' Total Length of
Bwd Packets', 'Flow Bytes/s', ' Flow Packets/s', ' Fwd Header Length', ' Bwd Header Length', ' Min Packet
Length', ' Max Packet Length', ' Average Packet Size', ' Avg Fwd Segment Size',' Avg Bwd Segment Size', '
Label']]
# Exportando base de treinamento e teste
from sklearn.model_selection import train_test_split
# Divido a base em treino e teste
X_, y_ = base.iloc[:,:-1], base.iloc[:, -1]# Aplico o holdout
X_train, X_test, y_train, y_test = train_test_split(X_, y_, test_size=0.3, random_state=1)
# Exporto a base de treinamento em CSV
X_train['Label'] = y_train
X_train.to_csv('base_treinamento.csv')
# Exporto a base de teste em CSV
X_test['Label'] = y_test
X_test.to_csv('base_teste.csv')
