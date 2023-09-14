const inputType = document.getElementById('input-type');
    const inputLabel = document.getElementById('input-label');

    inputType.addEventListener('change', (event) => {
        switch (event.target.value) {
            case 'drug_name':
                inputLabel.textContent = 'Give me a Name to Test, Stay Safe';
                break;
            case 'chembl_id':
                inputLabel.textContent = 'Share that Chembl ID for Quality Check';
                break;
            case 'smiles':
                inputLabel.textContent = 'Enter the SMILES Code, Let\'s Test';
                break;
            default:
                inputLabel.textContent = 'I know you\'re K, but what more than that?';
                break;
        }
    });