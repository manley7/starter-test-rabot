## story_greet
* salutation
	- utter_rep_salutation
	- utter_rep_need
	
## story_goodbye
* aurevoir
	- utter_aurevoir
	- action_restart

## story_thanks
* merci
	- utter_rep_merci
	- utter_rep_need

## Generated Story 5417591655620979859
* demande_de_virement
    - utter_ask_montant_virement
* demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
    - slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_beneficiare
* demande_de_virement{"DESTINATAIRE": "Georges"}
    - slot{"DESTINATAIRE": "Georges"}
    - utter_rep_virement_unit
* affirmation
    - utter_rep_confirmation_virement_unit
    - utter_rep_final

## Generated Story 5417591655620979859
* demande_de_virement
    - utter_ask_montant_virement
* demande_de_virement{"PRIX": "1000"}
    - slot{"PRIX": "1000"}
    - utter_ask_beneficiare
* demande_de_virement{"DESTINATAIRE": "Georges"}
    - slot{"DESTINATAIRE": "Georges"}
    - utter_rep_virement
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final

## Generated Story 343630072383034614
* salutation
    - utter_rep_salutation
    - utter_rep_need
* demande_de_credit{"PRIX": "500"}
    - slot{"PRIX": "500"}
    - utter_ask_montant_beneficiaire
* demande_de_virement{"DESTINATAIRE": "Marie"}
    - slot{"DESTINATAIRE": "Marie"}
    - utter_rep_virement
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final

## story_virement personne
* demande_de_virement
    - utter_ask_montant_virement
* demande_de_virement{"PRIX": "100 000"}
    - slot{"PRIX": "100 000"}
    - utter_ask_montant_beneficiaire	
* demande_de_virement{"DESTINATAIRE": "Didier"}
    - slot{"DESTINATAIRE": "Didier"}
    - utter_rep_virement	
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final	
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart

## story_virement prix_personne
* demande_de_virement{"PRIX": "100 000", "DESTINATAIRE": "Didier"}
	- slot{"PRIX": "100 000"}
	- slot{"DESTINATAIRE": "Didier"}
    - utter_rep_virement	
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final	
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart

## story_virement personne_seul
* demande_de_virement{"DESTINATAIRE": "Didier"}
	- slot{"DESTINATAIRE": "Didier"}
    - utter_ask_beneficiare_montant
* demande_de_virement{"PRIX": "100 000"}
    - slot{"PRIX": "100 000"}
    - utter_rep_virement	
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final	
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart
	
## story_virement prix_seul
* demande_de_virement{"PRIX": "100 000"}
    - slot{"PRIX": "100 000"}
    - utter_ask_montant_beneficiaire	
* demande_de_virement{"DESTINATAIRE": "Didier"}
    - slot{"DESTINATAIRE": "Didier"}
    - utter_rep_virement	
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final	
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart
	
	
## Generated Story -1616383393649699221
* demande_de_credit{"ARGENT": "argent"}
    - utter_ask_prix
* demande_de_credit{"PRIX": "100 000"}
    - slot{"PRIX": "200"}
    - utter_rep_credit_prix
* affirmation
    - utter_rep_confirmation_credit
    - utter_rep_final
* affirmation
    - action_restart
    - utter_rep_need

## Generated Story 343630072383034614
* salutation
    - utter_rep_salutation
    - utter_rep_need
* demande_de_credit{"PRIX": "500"}
    - slot{"PRIX": "500"}
    - utter_ask_montant_beneficiaire
* demande_de_virement{"DESTINATAIRE": "Marie"}
    - slot{"DESTINATAIRE": "Marie"}
    - utter_rep_virement
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final

	
## Stories1
* salutation
    - utter_rep_salutation
    - utter_rep_need
* Perte_de_carte_bancaire{"CB": "carte bleue"}
    - slot{"CB": "carte bleue"}
    - utter_ask_opposition
* affirmation
    - utter_rep_opposition
    - utter_rep_final
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart


## Stories2
* salutation
    - utter_rep_salutation
    - utter_rep_need
* demande_de_credit
    - utter_ask_type_achat
* demande_de_credit{"TYPE-ACHAT": "un appartement"}
    - slot{"TYPE-ACHAT": "un appartement"}
    - utter_ask_prix
* demande_de_credit{"PRIX": "100 000", "UNIT": "euros"}
    - slot{"PRIX": "100 000"}
    - slot{"UNIT": "euros"}
    - utter_rep_credit_prix_type_unit
* affirmation
    - utter_rep_confirmation_credit
    - utter_rep_final
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart


## Stories3
* salutation
    - utter_rep_salutation
    - utter_rep_need
* demande_de_credit{"TYPE-ACHAT": "une maison"}
    - slot{"TYPE-ACHAT": "une maison"}
    - utter_ask_prix
* demande_de_credit{"PRIX": "100 000", "UNIT": "euros"}
    - slot{"PRIX": "100 000"}
    - slot{"UNIT": "euros"}
    - utter_rep_credit_prix_type
* affirmation
    - utter_rep_confirmation_credit
    - utter_rep_final
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart

## Stories4
* salutation
    - utter_rep_salutation
    - utter_rep_need
* demande_de_virement
    - utter_ask_montant_virement
* demande_de_virement{"PRIX": "100 000", "UNIT": "euros"}
    - slot{"PRIX": "100 000"}
    - slot{"UNIT": "euros"}
    - utter_ask_beneficiare
* demande_de_virement{"DESTINATAIRE": "Mon pere"}
    - slot{"DESTINATAIRE": "Mon pere"}
    - utter_rep_virement
* affirmation
    - utter_rep_confirmation_virement
    - utter_rep_final
* affirmation
    - action_restart
    - utter_rep_need
* negation
    - action_restart


