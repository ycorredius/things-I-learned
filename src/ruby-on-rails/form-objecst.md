# Ruby File Objects

## This serves as representation of file objects. bases on [this blog](https://www.mintbit.com/blogunderstanding-the-differences-traditional-forms-vs-form-objects-in-rails#:~:text=Form%20Objects%20provide%20an%20elegant,and%20a%20traditional%20form%20approach.)

A form object is a object not controllered by a controller. It exists outside of a model has some benefits when it comes to flexibility.

Primary benefits:

1. Separation of Concerns - Separates form-related logic from the controller.
2. Resusablity - Forms are flexible and not set to be used by specific models.
3. Customization - Form objects allow custom validations and complex form logic to be encapsulated within an object.

```
  class FooForm
    include ActiveModel::model
    attr_accessor :bar, :bar2, :bar3

    validates :bar, presence: true

    def save
      if valid?
        ActiveRecord::Base.transaction do 
          foo = Foo.create!(bar: bar, bar2: bar2)
        end
      end
    end
  end
```

```
  class FooController < ApplicatonController
    def new
      @foo_form = FooForm.new
    end

    def create
      @foo_form = FooForm.new(foo_form_params)
      if @foo_form.save
        # It works
      else 
        # Boo didn't work
      end
    end

    private

    def foo_form_params
      params.require(:foo_form).permit(:bar, :bar2, :bar3)
    end
  end
```
