# Basic Devise Gem setup

## This is a simple guide meant to provide a genral over view for actual instructions refer to the [Devise Docs](https://github.com/heartcombo/devise "Devise Home")

1. Add `gem devise` to Gemfile.
2. Run command `bundle` or `bundle install`.
3. Now we install devise by running the command `rails g devise:install`.
4. Now that devise is installed we can run devise on the model we would like to work with with the command `rails g devise <MODEl>`.
5. Before we set the root I like to make a welcome route and index.
6. Set a root by going into config/routes.rb and typing `root to: "welcome#index`
7. Last set I like to allow to use devise default views for authentication by running command `rails g devise:views`.
