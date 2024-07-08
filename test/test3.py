# #! 普通用户查询信息
# @api.route("", methods=["GET"])
# @auth.login_required
# def get_user(uid):
#     # token 验证是否过期 是否合法
#     user = User.query.filter_by(id=uid).get_or_404()
#     # 当然可以，但是不够优雅
#     # r = {"nickname": user.nickname, "email": user.email}
#     # return jsonify(r)

#     return jsonify(user)

# #! 管理员查询信息
# @api.route("/<int:uid>", methods=["GET"])
# @auth.login_required
# def super_get_user(uid):
#     # token 验证是否过期 是否合法
#     user = User.query.filter_by(id=uid).get_or_404()
#     # 当然可以，但是不够优雅
#     # r = {"nickname": user.nickname, "email": user.email}
#     # return jsonify(r)

#     return jsonify(user)


# #! 普通用户删除自己的信息
# @api.route("", methods=["DELETE"])
# @auth.login_required
# def delete_user():
#     # 超权限（用户可以访问改接口是否拥有删除的操作）
#     # 用户1、2， 用户1token验证通过后，携带uid=2，就有可能删除用户2
#     # 不应该由用户传递uid删除用户，解决是从token中读取
#     # 在验证token的时候，use信息已存在g变量中，g变量是线程隔离的
#     uid = g.user.uid
#     with db.auto_commit():
#         user = User.query.filter_by(id=uid).first_or_404()
#         user.delete()

#     return DeleteSuccess()


# #! 超级管理员可根据uid删除他人信息
# @api.route("<int:uid>", methods=["DELETE"])
# @auth.login_required
# def delete_user():
#     # 管理员可以删除其他用户信息
#     uid = g.user.uid
#     with db.auto_commit():
#         user = User.query.filter_by(id=uid).first_or_404()
#         user.delete()

#     return DeleteSuccess()
