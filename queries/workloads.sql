 -- Update with correct collection instance

select collection_instance__c,
	   id,
	   name,
	   owner_name__c,
	   ownerId,
	   status__c,
	   workload_hours_numeric__c,
	   workload_id__c,
	   workload_priority_indicator__c,
	   workload_status__c
  from sf_prd.workload__c
 where (workload_id__c like 'CNP%')
	   and collection_instance__c = 'a031J00000cvgrwQAA';