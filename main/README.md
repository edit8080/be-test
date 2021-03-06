# π κ΅¬μ± API μ€λͺ

### request & response
    - request λ λͺ¨λ GET λ°©μμ νμ©ν©λλ€.
    - response λ λͺ¨λ JSON νμμΌλ‘ λ°μ΄ν°λ₯Ό λ°νν©λλ€.

### pagination <br />
κ° API λ κΈ°λ³Έμ μΌλ‘ νμ΄μ§λ€μ΄μμ΄ μ μ©λμ΄μμ΅λλ€. <br />
νμ΄μ§λ€μ΄μμ `page`μ `per_page` μμ±λͺμ ν΅ν μΏΌλ¦¬ μ€νΈλ§μΌλ‘ μ¬μ©ν  μ μμ΅λλ€. <br />
λ¨μΌ κ²°κ³Όλ₯Ό response νλ μΌλΆ API μλ νμ΄μ§λ€μ΄μμ΄ μ μ©λμ΄μμ§ μμ΅λλ€. (ex: idλ₯Ό ν΅ν κ²μ) <br />

## π· person

### 1. νμ μ ν΅κ³

<details>
<summary> μ μ²΄ νμ μ</summary>

```
API : /stat/person
response : { 'count': 0 }  
```
</details>

<details>
<summary> μ±λ³ νμ μ</summary>

```
API : /stat/person/gender/<string:gender>
response : { 'count': 0 }  
```
</details>

<details>
<summary> μΈμ’λ³ νμ μ</summary>

```
API : /stat/person/race/<string:race>
response : { 'count': 0 }  
```
</details>

<details>
<summary> λ―Όμ‘±λ³ νμ μ</summary>

```
API : /stat/person/ethnicity/<string:ethnicity>
response : { 'count': 0 }  
```
</details>

<details>
<summary> μ¬λ§ νμ μ</summary>

```
API : /stat/person/death
response : { 'count': 0 }  
```
</details>


### 2. νμ concept κ²μ

<details>
<summary> μ μ²΄ concept κ²μ</summary>

```
API : /person/concept
response : { 
  'concepts': {
    'gender': [],      
    'race': [],
    'ethnicity': []
  } 
}
```
</details>
<details>
<summary> μ±λ³ concept κ²μ</summary>

```
API : /person/concept/gender
response : { 
  'concepts': {
    'gender': [],      
  }
}
```
</details>
<details>
<summary> μΈμ’ concept κ²μ</summary>

```
API : /person/concept/race
response : { 
  'concepts': {
    'race': [],      
  }
}
```
</details>
<details>
<summary> λ―Όμ‘± concept κ²μ</summary>

```
API : /person/concept/ethnicity
response : { 
  'concepts': {
    'ethnicity': [],      
  }
}
```
</details>

### 3. νμ κ²μ

<details>
<summary> μ μ²΄ νμ κ²μ</summary>

```
API : /person
response : { 
  'person': [{
    'birth': 'Tue, 26 May 1987 00:00:00 GMT',
    'death': false,
    'ethnicity': 'No matching concept',
    'gender': 'MALE',
    'person_id': 2845932,
    'race': 'Asian'
    }, ...
  ],
  'page': 1, 
  'total': 1000
}
```
</details>

<details>
<summary> νμ ID κ²μ</summary>

```
API : /person/<string:person_id>
response : { 
  'person': {
    'birth': 'Fri, 18 Apr 1997 00:00:00 GMT',
    'death': false,
    'ethnicity': 'No matching concept',
    'gender': 'FEMALE',
    'person_id': 402435,
    'race': 'White'
  }
}  
```
</details>

<details>
<summary> μ±λ³ νμ κ²μ</summary>

```
API : /person/gender/<string:gender>
response : { 
  'person': [{
    'birth': 'Tue, 26 May 1987 00:00:00 GMT',
    'death': false,
    'ethnicity': 'No matching concept',
    'gender': 'MALE',
    'person_id': 2845932,
    'race': 'Asian'
    }, ...
  ],
  'page': 1, 
  'total': 1000
}
```
</details>

<details>
<summary> μΈμ’λ³ νμ κ²μ</summary>

```
API : /person/race/<string:race>
response : { 
  'person': [{
    'birth': 'Tue, 26 May 1987 00:00:00 GMT',
    'death': false,
    'ethnicity': 'No matching concept',
    'gender': 'MALE',
    'person_id': 2845932,
    'race': 'Asian'
    }, ...
  ],
  'page': 1, 
  'total': 1000
}
```
</details>

<details>
<summary> λ―Όμ‘±λ³ νμ κ²μ</summary>

```
API : /person/ethnicity/<string:ethnicity>
response : { 
  'person': [{
    'birth': 'Tue, 26 May 1987 00:00:00 GMT',
    'death': false,
    'ethnicity': 'No matching concept',
    'gender': 'MALE',
    'person_id': 2845932,
    'race': 'Asian'
    }, ...
  ],
  'page': 1, 
  'total': 1000
} 
```
</details>

<details>
<summary> μ¬λ§λ³ νμ κ²μ</summary>

```
API : /person/death
Query String: <boolean:isDead> (ex : /person/dead?isDead=true)
response : { 
  'person': [{
    'birth': 'Tue, 26 May 1987 00:00:00 GMT',
    'death': false,
    'ethnicity': 'No matching concept',
    'gender': 'MALE',
    'person_id': 2845932,
    'race': 'Asian'
    }, ...
  ],
  'page': 1, 
  'total': 1000
} 
```
</details>


## π₯ visit_occurrence

### 1. λ°©λ¬Έ μ ν΅κ³

<details>
<summary> μ νλ³ λ°©λ¬Έ μ</summary>

```
API : /stat/visit/type/<string:type>
response : { 'count': 0 } 
```
</details>

<details>
<summary> μ±λ³ λ°©λ¬Έ μ</summary>

```
API : /stat/visit/gender/<string:gender>
response : { 'count': 0 } 
```
</details>

<details>
<summary> μΈμ’λ³ λ°©λ¬Έ μ</summary>

```
API : /stat/visit/race/<string:race>
response : { 'count': 0 }  
```
</details>

<details>
<summary> λ―Όμ‘±λ³ λ°©λ¬Έ μ</summary>

```
API : /stat/visit/ethnicity/<string:ethnicity>
response : { 'count': 0 } 
```
</details>

<details>
<summary> μ°λ Ήλ(10μΈ λ¨μ)λ³ λ°©λ¬Έ μ</summary>

```
API : /stat/visit/age/<int:age_unit>
response : { 'count': 0 } 
```
</details>


### 2. λ°©λ¬Έ concept κ²μ

<details>
<summary> μ μ²΄ concept</summary>

```
API : /visit/concept
response : { 
  'concepts': {
      'type': [
          'Inpatient Visit',
          'Outpatient Visit',
          'Emergency Room Visit'
      ]
  }
}
```
</details>

<details>
<summary> λ°©λ¬Έ μ ν concept κ²μ</summary>

```
API : /visit/concept/type
response : { 
  'concepts': {
      'type': [
          'Inpatient Visit',
          'Outpatient Visit',
          'Emergency Room Visit'
      ]
  }
}
```
</details>

### 3. λ°©λ¬Έ κ²μ

<details>
<summary> μ νλ³ λ°©λ¬Έ κ²μ</summary>

```
API : /visit/type/<string:type>
response : { 
  'visits': [
      {
        'person': {
            'birth': 'Wed, 05 Feb 1936 00:00:00 GMT',
            'death': true,
            'ethnicity': 'No matching concept',
            'gender': 'FEMALE',
            'person_id': 112670,
            'race': 'White'
        },
        'visit_concept_name': 'Inpatient Visit',
        'visit_end_datetime': 'Wed, 06 Feb 1985 20:28:07 GMT',
        'visit_occurrence_id': 645620,
        'visit_start_datetime': 'Tue, 05 Feb 1985 16:28:07 GMT'
      }, ...
  ],
  'page': 1,
  'total': 1309,
}
```
</details>

<details>
<summary> μ±λ³ λ°©λ¬Έ κ²μ</summary>

```
API : /visit/gender/<string:gender>
response : { 
  'visits': [
      {
        'person': {
            'birth': 'Wed, 05 Feb 1936 00:00:00 GMT',
            'death': true,
            'ethnicity': 'No matching concept',
            'gender': 'FEMALE',
            'person_id': 112670,
            'race': 'White'
        },
        'visit_concept_name': 'Inpatient Visit',
        'visit_end_datetime': 'Wed, 06 Feb 1985 20:28:07 GMT',
        'visit_occurrence_id': 645620,
        'visit_start_datetime': 'Tue, 05 Feb 1985 16:28:07 GMT'
      }, ...
  ],
  'page': 1,
  'total': 1309,
}
```
</details>

<details>
<summary> μΈμ’λ³ λ°©λ¬Έ κ²μ</summary>

```
API : /visit/race/<string:race>
response : { 
  'visits': [
      {
        'person': {
            'birth': 'Wed, 05 Feb 1936 00:00:00 GMT',
            'death': true,
            'ethnicity': 'No matching concept',
            'gender': 'FEMALE',
            'person_id': 112670,
            'race': 'White'
        },
        'visit_concept_name': 'Inpatient Visit',
        'visit_end_datetime': 'Wed, 06 Feb 1985 20:28:07 GMT',
        'visit_occurrence_id': 645620,
        'visit_start_datetime': 'Tue, 05 Feb 1985 16:28:07 GMT'
      }, ...
  ],
  'page': 1,
  'total': 1309,
}
```
</details>

<details>
<summary> λ―Όμ‘±λ³ λ°©λ¬Έ κ²μ</summary>

```
API : /visit/ethnicity/<string:ethnicity>
response : { 
  'visits': [
      {
        'person': {
            'birth': 'Wed, 05 Feb 1936 00:00:00 GMT',
            'death': true,
            'ethnicity': 'No matching concept',
            'gender': 'FEMALE',
            'person_id': 112670,
            'race': 'White'
        },
        'visit_concept_name': 'Inpatient Visit',
        'visit_end_datetime': 'Wed, 06 Feb 1985 20:28:07 GMT',
        'visit_occurrence_id': 645620,
        'visit_start_datetime': 'Tue, 05 Feb 1985 16:28:07 GMT'
      }, ...
  ],
  'page': 1,
  'total': 1309,
}
```
</details>

<details>
<summary> λ°©λ¬Έμ μ°λ Ήλ(10μΈ λ¨μ)λ³ λ°©λ¬Έ μ</summary>

```
API : /visit/age/<int:age_unit>
response : { 
  'visits': [
      {
        'person': {
            'birth': 'Wed, 05 Feb 1936 00:00:00 GMT',
            'death': true,
            'ethnicity': 'No matching concept',
            'gender': 'FEMALE',
            'person_id': 112670,
            'race': 'White'
        },
        'visit_concept_name': 'Inpatient Visit',
        'visit_end_datetime': 'Wed, 06 Feb 1985 20:28:07 GMT',
        'visit_occurrence_id': 645620,
        'visit_start_datetime': 'Tue, 05 Feb 1985 16:28:07 GMT'
      }, ...
  ],
  'page': 1,
  'total': 1309,
}
```
</details>

## π drug_exposure

### 1. μμ½ν concept κ²μ

<details>
<summary> μμ½ν concept κ²μ</summary>

```
API : /drug/concept
response : { 
  'concepts': {
    'drug_exposure': [
        'nitroglycerin 0.4 MG/ACTUAT Mucosal Spray',
        'alteplase 100 MG Injection',
        '{28 (norethindrone 0.35 MG Oral Tablet) } Pack [Camila 28 Day]',
        'penicillin V potassium 250 MG Oral Tablet',
        'prednisone 5 MG Oral T,
        ...
    ]
  }
}
```
</details>

### 2. μμ½ν κ²μ

<details>
<summary> μμ½ν ID κ²μ</summary>

```
API : /drug/<string:drug_id>
response : { 
 'drug': {
    'drug_exposure_end_datetime': 'Tue, 26 Feb 2002 13:27:57 GMT',
    'drug_exposure_id': 87678794,
    'drug_exposure_name': '3 ML amiodarone hydrochloride 50 MG/ML Prefilled Syringe',
    'drug_exposure_start_datetime': 'Tue, 26 Feb 2002 13:12:57 GMT',
    'person_id': 1553757,
    'visit_occurrence_id': 14893229
  }
}
```
</details>

<details>
<summary> μμ½νλͺ κ²μ</summary>

```
API : /drug
Query String: <string:name> (ex : /drug?name=hydro)
response : { 
 'drugs': [
    {
        'drug_exposure_end_datetime': 'Tue, 26 Feb 2002 13:27:57 GMT',
        'drug_exposure_id': 87678794,
        'drug_exposure_name': '3 ML amiodarone hydrochloride 50 MG/ML Prefilled Syringe',
        'drug_exposure_start_datetime': 'Tue, 26 Feb 2002 13:12:57 GMT',
        'person_id': 1553757,
        'visit_occurrence_id': 14893229
    }, ...
  ],
  'page': 1,
  'total': 10106
}
```
</details>


## π¨ββ condition_occurrence

### 1. μ§λ¨ concept κ²μ

<details>
<summary> μ§λ¨λͺ concept κ²μ</summary>

```
API : /condition/concept
response : {
  'concepts': {
    'condition_concept': [
        'Traumatic brain injury',
        'Fracture subluxation of wrist',
        'Epilepsy',
        'Pre-eclampsia',
        'Atrial fibrillation',
        ...
    ]
  }
}
```
</details>

### 2. μ§λ¨ κ²μ

<details>
<summary> μ§λ¨ ID κ²μ</summary>

```
API : /condition/<string:condition_id>
response : {
  'condition': {
    'condition_concept_name': 'Chill',
    'condition_end_datetime': 'Sat, 18 Apr 2020 00:00:00 GMT',
    'condition_occurrence_id': 11162529,
    'condition_start_datetime': 'Thu, 19 Mar 2020 00:00:00 GMT',
    'person_id': 886110,
    'visit_occurrence_id': 31254226
  }
}
```
</details>

<details>
<summary> λ³λͺ κ²μ</summary>

```
API : /condition
Query String: <string:name> (ex : /condition?name=chill)
response : {
  'conditions': [
      {
          'condition_concept_name': 'Chill',
          'condition_end_datetime': 'Sat, 18 Apr 2020 00:00:00 GMT',
          'condition_occurrence_id': 11162529,
          'condition_start_datetime': 'Thu, 19 Mar 2020 00:00:00 GMT',
          'person_id': 886110,
          'visit_occurrence_id': 31254226
      }, ...
  ],
  'page': 1,
  'total': 99
}
```
</details>
