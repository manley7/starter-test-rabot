## story_greet
* salutation
    - utter_rep_salutation
    - utter_rep_need
	
## story_goodbye
* aurevoir
    - utter_aurevoir
    - action_restart
	
## Generated Story -2942731702921727471
* merci
    - utter_rep_merci
    - action_restart

## Generated Story -2028799192447428117
* None
    - utter_default
   

## Story non
* negation
    - utter_negation
    - action_restart

## solde restart
* solde
    - action_rep_solde
    - utter_rep_final
    - action_restart
 
## story demande virement sans information
* demande_de_virement
    - utter_ask_montant_virement
* demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_montant_beneficiaire_unit
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
    - action_nlg
    - utter_rep_virement_unit
* affirmation
    - action_virement
    - utter_rep_final	
    - action_restart

## story demande virement sans information negatif
* demande_de_virement
    - utter_ask_montant_virement
* demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_montant_beneficiaire_unit
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
    - action_nlg
    - utter_rep_virement_unit
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart

## story demande virement avec montant
* demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_montant_beneficiaire_unit
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
    - action_nlg
    - utter_rep_virement_unit
* affirmation
    - action_virement
    - utter_rep_final	
    - action_restart

## story demande virement avec montant negatif
* demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_montant_beneficiaire_unit
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
    - action_nlg
    - utter_rep_virement_unit
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart

## story demande virement avec beneficiaire
* demande_de_virement{"DESTINATAIRE": "Georges"}
    - slot{"DESTINATAIRE": "Georges"}
    - utter_ask_beneficiare_montant
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - action_nlg
    - utter_rep_virement_unit
* affirmation
    - action_virement    
    - utter_rep_final	
    - action_restart

## story virement destinataire negatif
* demande_de_virement{"DESTINATAIRE": "Georges"}
    - slot{"DESTINATAIRE": "Georges"}
    - utter_ask_beneficiare_montant
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - action_nlg
    - utter_rep_virement_unit
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart

## story demande virement montant et beneficiaire
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
    - action_nlg
    - utter_rep_virement_unit
* affirmation
    - action_virement
    - utter_rep_final
    - action_restart

## story demande virement montant et beneficiaire negatif
* demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
    - action_nlg
    - utter_rep_virement_unit
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart

## story perte_carte bancaire
* Perte_de_carte_bancaire{"CB": "CB"}
    - slot{"CB": "CB"}
    - utter_ask_opposition
* affirmation
    - action_opposition
    - utter_rep_final
    - action_restart

## story perte_carte bancaire negatif
* Perte_de_carte_bancaire{"CB": "CB"}
    - slot{"CB": "CB"}
    - utter_ask_opposition
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart


## story demande opposition carte
* opposition{"CB": "CB"}
    - slot{"CB": "CB"}
    - utter_ask_opposition
* affirmation
    - action_opposition
    - utter_rep_final
    - action_restart

## story demande opposition carte negatif
* opposition{"CB": "CB"}
    - slot{"CB": "CB"}
    - utter_ask_opposition
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart

## story demande opposition simple
* opposition
    - utter_ask_opposition
* affirmation
    - action_opposition    
    - utter_rep_final
    - action_restart

## story demande opposition simple negatif
* opposition
    - utter_ask_opposition
* negation
    - utter_rep_virement_annule
    - utter_rep_final
    - action_restart


## story rib
* envoi_rib
    - utter_rib
* email{"EMAIL": "souleymane.belhouchat@pwc.com"}
    - slot{"EMAIL": "souleymane.belhouchat@pwc.com"}
    - action_send_email
    - utter_rep_final
    - action_restart
