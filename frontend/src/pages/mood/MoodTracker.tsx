import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'

const moodData = [
  { date: 'Mon', mood: 3 },
  { date: 'Tue', mood: 4 },
  { date: 'Wed', mood: 2 },
  { date: 'Thu', mood: 5 },
  { date: 'Fri', mood: 4 },
  { date: 'Sat', mood: 6 },
  { date: 'Sun', mood: 5 }
]

export default function MoodTracker() {
  const [selectedMood, setSelectedMood] = useState<number | null>(null)

  return (
    <div className="container mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold">Mood Tracker</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>Today's Mood</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex justify-between mb-4">
            {[1, 2, 3, 4, 5].map((mood) => (
              <Button
                key={mood}
                variant={selectedMood === mood ? 'default' : 'outline'}
                onClick={() => setSelectedMood(mood)}
              >
                {mood}
              </Button>
            ))}
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Mood History</CardTitle>
        </CardHeader>
        <CardContent className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={moodData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis domain={[0, 10]} />
              <Tooltip />
              <Line type="monotone" dataKey="mood" stroke="#3B82F6" />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  )
}