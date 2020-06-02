from app.database.models import User


class MongoDAO:

    @staticmethod
    def get_all_enrolled_classes(user_id):
        aggregation = [
            {
                '$lookup': {
                    'from': 'enrollment',
                    'localField': 'user_id',
                    'foreignField': 'user_id',
                    'as': 'r1'
                }
            }, {
                '$unwind': {
                    'path': '$r1',
                    'includeArrayIndex': 'r1_id',
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$lookup': {
                    'from': 'course',
                    'localField': 'r1.courseID',
                    'foreignField': 'courseID',
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r2',
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'user_id': user_id
                }
            }, {
                '$sort': {
                    'courseID': 1
                }
            }
        ]

        return list(User.objects.aggregate(*aggregation))
