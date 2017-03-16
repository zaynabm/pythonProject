{% extends ../base.html %}


function leaveGroup()
{

		$.ajax({
       groupName="openSource"
       groupID=db.groups.find_one({"name":groupName},{"_id":1})
       print(groupID)
       for key, val in groupID.items():
               #print(val)
               userID=2
               db.groups.update(
                          {"_id":val},
                          {"$push":{"members":userID}}
                       )
               db.users.update(
                          {"_id":userID},
                          {"$push":{"Groups":val}}
                       )

		$("#city").text(res.name);
		$("#weather").html(res.weather[0].main+"</br>"+Math.round((res.main.temp_max-273))+"&nbsp;&nbsp;&nbsp;"+Math.round((res.main.temp_min-273)));

    return res;
		}
		})
}
