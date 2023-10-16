set -e

echo "Creating user:"

mongosh <<EOF
db = db.getSiblingDB('admin')

db.createUser({
  user: '$MONGO_ADMIN_USERNAME',
  pwd: '$MONGO_ADMIN_PASSWORD',
  roles: [{ role: 'dbOwner', db: 'admin' }],
});

EOF