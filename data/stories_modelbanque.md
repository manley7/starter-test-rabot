

## story_demande_credit_001
* demande_de_credit
    - utter_ask_type_achat
* demande_de_credit{"$TYPE-ACHAT": "une maison"}
    - utter_ask_prix
* demande_de_credit{"$PRIX": "200 000"}
    - utter_rep_credit
* affirm
    - utter_rep_credit
* deny
    - action_restart

## story_perte_carte_001
* Perte_de_carte_bancaire
    - utter_ask_opposition
* affrim
    - utter_rep_opposition
* deny
    - action_restart

## Generated Story -3836338165568618545
* demande_de_credit{"$TYPE-ACHAT": "une maison"}
    - slot{"$TYPE-ACHAT": "une maison"}
    - utter_ask_prix
* affirm{"$PRIX": "100 000", "$UNIT": "euros"}
    - slot{"$PRIX": "100 000"}
    - slot{"$UNIT": "euros"}
    - utter_rep_credit

