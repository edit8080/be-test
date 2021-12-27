# 🔎 구성 API 설명

### request & response
    - request 는 모두 GET 방식을 활용합니다.
    - response 는 모두 JSON 형식으로 데이터를 반환합니다.

### pagination <br />
각 API 는 기본적으로 페이지네이션이 적용되어있습니다. <br />
페이지네이션은 `page`와 `per_page` 속성명을 통한 쿼리 스트링으로 사용할 수 있습니다. <br />
단일 결과를 response 하는 일부 API 에는 페이지네이션이 적용되어있지 않습니다. (ex: id를 통한 검색) <br />

## person

### 1. 환자 수 통계

<details>
<summary> 전체 환자 수</summary>

```
API : /stat/person
response : { 'count': 0 }  
```
</details>

<details>
<summary> 성별 환자 수</summary>

```
API : /stat/person/gender/<string:gender>
response : { 'count': 0 }  
```
</details>

<details>
<summary> 인종별 환자 수</summary>

```
API : /stat/person/race/<string:race>
response : { 'count': 0 }  
```
</details>

<details>
<summary> 민족별 환자 수</summary>

```
API : /stat/person/ethnicity/<string:ethnicity>
response : { 'count': 0 }  
```
</details>

<details>
<summary> 사망 환자 수</summary>

```
API : /stat/person/death
response : { 'count': 0 }  
```
</details>


### 2. 환자 concept 검색

<details>
<summary> 전체 concept 검색</summary>

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
<summary> 성별 concept 검색</summary>

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
<summary> 인종 concept 검색</summary>

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
<summary> 민족 concept 검색</summary>

```
API : /person/concept/ethnicity
response : { 
  'concepts': {
    'ethnicity': [],      
  }
}
```
</details>

### 3. 환자 검색

<details>
<summary> 전체 환자 검색</summary>

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
<summary> 환자 ID 검색</summary>

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
<summary> 성별 환자 검색</summary>

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
<summary> 인종별 환자 검색</summary>

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
<summary> 민족별 환자 검색</summary>

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
<summary> 사망별 환자 검색</summary>

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


## visit_occurrence

### 1. 방문 수 통계

<details>
<summary> 유형별 방문 수</summary>

```
API : /stat/visit/type/<string:type>
response : { 'count': 0 } 
```
</details>

<details>
<summary> 성별 방문 수</summary>

```
API : /stat/visit/gender/<string:gender>
response : { 'count': 0 } 
```
</details>

<details>
<summary> 인종별 방문 수</summary>

```
API : /stat/visit/race/<string:race>
response : { 'count': 0 }  
```
</details>

<details>
<summary> 민족별 방문 수</summary>

```
API : /stat/visit/ethnicity/<string:ethnicity>
response : { 'count': 0 } 
```
</details>

<details>
<summary> 연령대(10세 단위)별 방문 수</summary>

```
API : /stat/visit/age/<int:age_unit>
response : { 'count': 0 } 
```
</details>


### 2. 방문 concept 검색

<details>
<summary> 전체 concept</summary>

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
<summary> 방문 유형 concept 검색</summary>

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

### 3. 방문 검색

<details>
<summary> 유형별 방문 검색</summary>

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
<summary> 성별 방문 검색</summary>

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
<summary> 인종별 방문 검색</summary>

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
<summary> 민족별 방문 검색</summary>

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
<summary> 방문시 연령대(10세 단위)별 방문 수</summary>

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

## drug_exposure

### 1. 의약품 concept 검색

<details>
<summary> 의약품 concept 검색</summary>

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

### 2. 의약품 검색

<details>
<summary> 의약품 ID 검색</summary>

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
<summary> 의약품명 검색</summary>

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


## condition_occurrence

### 1. 진단 concept 검색

<details>
<summary> 진단명 concept 검색</summary>

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

### 2. 진단 검색

<details>
<summary> 진단 ID 검색</summary>

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
<summary> 병명 검색</summary>

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
