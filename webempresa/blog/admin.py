"""Blog admin."""

# Django modules
from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 
                       'updated'
                       )

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 
                       'updated'
                       )
    
    """Columns to show"""
    list_display = ('title', 
                    'author', 
                    'published',
                    'post_categories',
                    )
    
    """Ordering by field or fields"""
    ordering = ('author', 
                'published'
                )
    
    """Search field... To look for author must user author__username"""
    search_fields = ('title', 
                     'content', 
                     'author__username', 
                     'categories__name',
                     )
    
    """By date"""
    date_hierarchy = 'published'
    
    list_filter = ('author__username', 
                   'categories__name',
                   )
    
    """Defining our own categories"""
    def post_categories(self, obj):
        # Entering to ManyToManyField
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías'
        
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
