# # Create database



# # Registration route and view
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         # Check if the username or email is already registered
#         existing_user = User.query.filter_by(username=username).first()
#         existing_email = User.query.filter_by(email=email).first()

#         if existing_user:
#             flash('Username already taken. Please choose another.')
#         elif existing_email:
#             flash('Email address already registered.')
#         else:
#             # Hash the password before storing it
#             hashed_password = generate_password_hash(password, method='sha256')
#             new_user = User(username=username, email=email, password=hashed_password)
#             session.add(new_user)
#             session.commit()
#             flash('Registration successful. You can now log in.')
#             return redirect(url_for('login'))

#     return render_template('register.html')

# # Login route and view
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         user = User.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password, password):
#             flash('Login successful!')

#             # Implement session management or JWT authentication here
#         else:
#             flash('Login failed. Check your credentials.')

#     return render_template('login.html')

# # Logout route
# @app.route('/logout')
# def logout():
#     # Implement session/logout logic here
#     flash('Logout successful.')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)
