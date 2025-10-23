import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { useNavigate } from 'react-router-dom'

export default function Dashboard() {
  const navigate = useNavigate()

  return (
    <div className="container mx-auto p-4 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <Button onClick={() => navigate('/settings')}>Settings</Button>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {/* Mood Card */}
        <Card>
          <CardHeader>
            <CardTitle>Today's Mood</CardTitle>
            <CardDescription>How are you feeling today?</CardDescription>
          </CardHeader>
          <CardContent>
            <Button variant="outline" className="w-full" onClick={() => navigate('/mood')}>
              Log Your Mood
            </Button>
          </CardContent>
        </Card>

        {/* Quick Tip Card */}
        <Card>
          <CardHeader>
            <CardTitle>Today's Tip</CardTitle>
            <CardDescription>Helpful advice for your day</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              Take a deep breath and focus on the present moment.
            </p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        {/* Recent Journal Entries */}
        <Card>
          <CardHeader>
            <div className="flex justify-between items-center">
              <CardTitle>Recent Journal Entries</CardTitle>
              <Button variant="ghost" size="sm" onClick={() => navigate('/journal')}>
                View All
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <p className="text-sm text-muted-foreground">
                No recent entries. Start journaling to see your thoughts here.
              </p>
            </div>
          </CardContent>
        </Card>

        {/* Chat with AI */}
        <Card>
          <CardHeader>
            <CardTitle>Chat with AI</CardTitle>
            <CardDescription>Get support from your AI coach</CardDescription>
          </CardHeader>
          <CardContent>
            <Button className="w-full" onClick={() => navigate('/chat')}>
              Start Chat
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}