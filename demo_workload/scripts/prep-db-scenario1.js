db = db.getSiblingDB("PresidentialCampaigns");
db.adminCommand({enableSharding:"PresidentialCampaigns"});
db.createCollection("donations");
db.adminCommand({shardCollection:"PresidentialCampaigns.donations", key:{"candidate_name":"hashed"},numInitialChunks:8});