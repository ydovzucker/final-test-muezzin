
import base64

from elastic.connection_elastic import  get_es_client

class Classification:
     def __init__(self):
         self.es = get_es_client()

     def decode_encrypted_string(self,encoded_message):
         #decodes to bytes

         decoded_message_bytes = base64.b64decode(encoded_message)

         # Converts the decoded bytes to a string
         decoded_message_str = decoded_message_bytes.decode('utf-8')
         return decoded_message_str
     def bds_percent(self,txt,hostile_list,semi_hostile_list): # calculates how hostile this text is
         list_of_words = txt.split(" ")
         count_total_words = len(list_of_words)
         count_alarming_words = 0
         for i  in range(len(list_of_words)): #loop through the list to find how many alarming words
             if list_of_words[i] in hostile_list or list_of_words[i] + " " + list_of_words[i + 1] in hostile_list:
                 count_alarming_words += 2
             elif list_of_words[i] in semi_hostile_list or list_of_words[i] + " " + list_of_words[i + 1] in semi_hostile_list:
                 count_alarming_words += 1
         bds_percent_in_text = count_alarming_words / count_total_words * 100
         rounded_percent = round(bds_percent_in_text,2)
         return rounded_percent
     def is_bds(self,percent_bds):
         threshold = 10
         return percent_bds > threshold
     def threat_level(self,bds_percent):
         bds_threat_level = ""
         if bds_percent < 10:
             bds_threat_level = "none"
         elif bds_percent < 15:
             bds_threat_level = "medium"
         else:
             bds_threat_level = "high"
         return bds_threat_level
     def insert_values_into_document(self,doc,index_name,document_id):

         response = self.es.update(
             index=index_name,
             id=document_id,
             body={
                 "doc": doc
             }
         )
         return response







if __name__ == "__main__":
    c = Classification()
    print(c.decode_encrypted_string(encrypted_hostile_list))
    print(c.decode_encrypted_string(encrypted_semi_hostile_list))