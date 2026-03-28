from django.db import models
from django.contrib.auth.models import User

# Book Post Model
class Post(models.Model):
    # Relates the book directly to the Django User who posted it
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_owned')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100) # The author of the book itself
    phone = models.CharField(max_length=13, blank=True)
    cover = models.ImageField(upload_to="static/sagar", blank=True, null=True)
    info = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, 
        choices=[('Available', 'Available'), ('Pending', 'Pending'), ('Traded', 'Traded')], 
        default='Available'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gallery"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.title} (Owned by {self.owner.username})"

# Trade Request Model to handle the "Barter" functionality
class TradeRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trade_requests_sent')
    book_requested = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='trade_requests_received')
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, 
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], 
        default='Pending'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.requester.username} for {self.book_requested.title}"
