db = db.getSiblingDB("campaigns");
collection = db.getCollection("donations"+col);
for(i=0; i < 2000; i++){
collection.find({contributor_occupation:"INVESTMENT BANKER"}).sort({amount:-1}).toArray();
collection.find({contributor_occupation:"INVESTMENT BANKER"}).toArray();
collection.find({contributor_occupation:"INVESTMENT BANKER"}).sort({candidate_name:1}).toArray();
};
