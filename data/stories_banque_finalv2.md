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
    - utter_rep_need
	- action_restart

## Generated Story -2028799192447428117
* None
    - utter_default
> need_help

## Checkpoint restart
> need_help
	- utter_rep_need
	- action_restart

## solde restart

* solde
	- action_rep_solde
	- utter_rep_solde
	- utter_rep_final
* affirmation
> need_help
* negation
- action_restart
- 
## story demande virement sans information
*demande_de_virement
	- utter_ask_montant_virement
*demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
	- slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_montant_beneficiaire_unit
*demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
	- slot{"DESTINATAIRE": "Didier"}
	- utter_rep_virement_unit
* affirmation
	- utter_rep_confirmation_virement_unit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story demande virement avec montant
*demande_de_virement{"PRIX": "1000", "UNIT": "euros"}
	- slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - utter_ask_montant_beneficiaire_unit
*demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
	- slot{"DESTINATAIRE": "Didier"}
	- utter_rep_virement_unit
* affirmation
	- utter_rep_confirmation_virement_unit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story demande virement avec beneficiaire
*demande_de_virement{"DESTINATAIRE": "Georges"}
    - slot{"DESTINATAIRE": "Georges"}
	- utter_ask_beneficiare_montant
*demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
	- slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
	- utter_rep_virement_unit
* affirmation
	- utter_rep_confirmation_virement_unit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story demande virement montant et beneficiaire
*demande_de_virement{"PRIX": "100", "DESTINATAIRE": "Didier", "UNIT": "euros"}
	- slot{"PRIX": "1000"}
    - slot{"UNIT": "euros"}
    - slot{"DESTINATAIRE": "Didier"}
	- utter_rep_virement_unit
* affirmation
	- utter_rep_confirmation_virement_unit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story demande de credit sans information
* demande_de_credit
    - utter_ask_prix
* demande_de_credit{"PRIX": "100 000", "UNIT": "euros"}
    - slot{"PRIX": "100 000"}
	- slot{"UNIT": "euros"}
    - utter_rep_credit_prix_unit
* affirmation
	- utter_rep_confirmation_credit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story demande de credit pour un projet
* demande_de_credit{"TYPE-ACHAT": "une voiture"}
    - slot{"TYPE-ACHAT": "une voiture"}
    - utter_ask_prix
* demande_de_credit{"PRIX": "2500", "UNIT": "euro"}
    - slot{"PRIX": "2500"}
    - slot{"UNIT": "euro"}
    - utter_rep_credit_prix_type_unit
* affirmation
	- utter_rep_confirmation_credit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story demande de credit avec montant
* demande_de_credit{"PRIX": "100 000", "UNIT": "euros"}
    - slot{"PRIX": "100 000"}
	- slot{"UNIT": "euros"}
    - utter_rep_credit_prix_unit
* affirmation
	- utter_rep_confirmation_credit
	- utter_rep_final	
* affirmation
> need_help
* negation
    - action_restart

## story perte_carte bancaire
* Perte_de_carte_bancaire{"CB": "CB"}
	- slot{"CB": "CB"}
	- utter_ask_opposition
* affirmation
	- utter_rep_opposition
	- utter_rep_final
* affirmation
> need_help
* negation
    - action_restart
	
## story demande opposition carte
* opposition{"CB": "CB"}
	- slot{"CB": "CB"}
	- utter_rep_opposition_cb
	- utter_rep_final
* affirmation
> need_help
* negation
    - action_restart

## story demande opposition simple
* opposition
	- utter_rep_opposition
	- utter_rep_final
* affirmation
> need_help
* negation
    - action_restart
