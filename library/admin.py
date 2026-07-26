from django.contrib import admin
from .models import Book, Member, Issue

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'available_copies', 'total_copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'user', 'membership_type', 'date_joined', 'is_active_member')
    search_fields = ('member_id', 'user__username')
    list_filter = ('membership_type', 'is_active_member')

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'issue_date', 'due_date', 'is_returned', 'fine_amount')
    list_filter = ('is_returned',)
    search_fields = ('book__title', 'member__member_id')