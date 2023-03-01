-- Update with correct collection instance
-- Update work item type?

select *
  from sf_prd.work_item__c
 where work_item_type__c in ('NPD - Collect')
	   and collection_instance__c = 'a031J00000cvgrwQAA';