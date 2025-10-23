import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

type JournalEntry = {
  id: string
  date: Date
  content: string
}

export default function Journal() {
  const [entries, setEntries] = useState<JournalEntry[]>([])
  const [newEntry, setNewEntry] = useState('')

  const handleAddEntry = () => {
    if (!newEntry.trim()) return
    const entry: JournalEntry = {
      id: Date.now().toString(),
      date: new Date(),
      content: newEntry
    }
    setEntries([entry, ...entries])
    setNewEntry('')
  }

  return (
    <div className="container mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold">Journal</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>New Entry</CardTitle>
        </CardHeader>
        <CardContent>
          <Textarea
            value={newEntry}
            onChange={(e) => setNewEntry(e.target.value)}
            placeholder="How are you feeling today?"
            className="min-h-[150px]"
          />
          <Button className="mt-4" onClick={handleAddEntry}>
            Save Entry
          </Button>
        </CardContent>
      </Card>

      <div className="space-y-4">
        {entries.map((entry) => (
          <Card key={entry.id}>
            <CardHeader>
              <CardTitle className="text-lg">
                {entry.date.toLocaleDateString()}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="whitespace-pre-line">{entry.content}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}